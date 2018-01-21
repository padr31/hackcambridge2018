import {Component, OnInit} from '@angular/core';
import {ApiService} from '../../../services/api.service';
import {Subscription} from 'rxjs/Subscription';

@Component({
  selector: 'histogram-component',
  templateUrl: 'histogram.component.html'
})

export class HistogramComponent implements OnInit {

  processSubscription: Subscription;
  apiService: ApiService;

  public chartType = 'bar';

  public emotions = ['anger', 'contempt', 'disgust', 'fear', 'happiness', 'neutral', 'sadness', 'surprise'];

  public chartDatasets: Array<any> = [{data: [], label: 'emotions'}];

  constructor(apiService: ApiService) {
    this.apiService = apiService;
  }

  public chartLabels: Array<any> = this.emotions;

  public chartColors: Array<any> = [
    {
      backgroundColor: 'rgba(151,187,205,0.2)',
      borderColor: 'rgba(151,187,205,1)',
      borderWidth: 2,
      pointBackgroundColor: 'rgba(151,187,205,1)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgba(151,187,205,1)'
    },
    {
      backgroundColor: 'rgba(255,187,205,0.2)',
      borderColor: 'rgba(255,0,205,1)',
      borderWidth: 2,
      pointBackgroundColor: 'rgba(151,187,205,1)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgba(151,187,205,1)'
    }
  ];

  public chartOptions: any = {
    responsive: true,
    scales: {
      yAxes: [{
        stacked: false
      }]
    },
    legend: {
      display: false
    },
    tooltips: {
      enabled: false
    }
  };

  ngOnInit() {
    this.processSubscription = this.apiService.imageChange.subscribe(
      data => {
        console.log('Got data in graph-component');
        this.chartDatasets[0].data = data.histogram;
        this.chartLabels = data.histogram_labels;
        console.log(this.chartDatasets);
        console.log(this.chartLabels);
      }
    );
  }

  ngOnDestroy() {
    this.processSubscription.unsubscribe();
  }

  public chartClicked(e: any): void {

  }

  public chartHovered(e: any): void {

  }

}
