import { Component, OnInit } from '@angular/core';
import { Subscription } from 'rxjs/Subscription';
import { ApiService } from '../../../services/api.service';

@Component({
    selector: 'graph-component',
    templateUrl: 'graph.component.html'
})
export class GraphComponent implements OnInit {
    
    processSubscription:Subscription;
    apiService:ApiService;
    
    public chartType:string = 'line';
        
    public chartDatasets:Array<any> = [
        {data: [], label: 'Happiness'}    
    ];

    constructor(apiService:ApiService) {
        this.apiService = apiService;
     }
    
    ngOnInit() { 
        this.processSubscription = this.apiService.imageChange.subscribe(
            data => {
                console.log("Got data in graph-component");
                this.chartDatasets = data.is;
                this.chartLabels = data.ts;
                console.log(this.chartDatasets);
                console.log(this.chartLabels);
            }
        );
    }

    public chartLabels:Array<any> = ['', '', '', '', '', '', '', '', '', ''];

    public chartColors:Array<any> = [
        {
            backgroundColor: 'rgba(151,187,205,0.2)',
            borderColor: 'rgba(151,187,205,1)',
            borderWidth: 2,
            pointBackgroundColor: 'rgba(151,187,205,1)',
            pointBorderColor: '#fff',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: 'rgba(151,187,205,1)'
        }
    ];

    public chartOptions:any = { 
        responsive: true,
        scales: {
            yAxes: [{
                stacked: true
            }]
        }
    };

    public chartClicked(e: any): void { 
            
    } 
    
    public chartHovered(e: any): void { 
            
    }
}