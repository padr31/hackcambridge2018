import { Component, OnInit } from '@angular/core';
import { Subscription } from 'rxjs/Subscription';
import { ApiService } from '../../../services/api.service';

@Component({
    selector: 'long-graph-component',
    templateUrl: 'long-graph.component.html'
})
export class LongGraphComponent implements OnInit {

    processSubscription:Subscription;
    apiService:ApiService;
    
    public chartType:string = 'line';
        
    public chartDatasets:Array<any> = [
        {data: [], label: 'isa'}    
    ];

    constructor(apiService:ApiService) {
        this.apiService = apiService;
     }
    
    ngOnInit() { 
        this.processSubscription = this.apiService.imageChange.subscribe(
            data => {
                console.log("Got data in graph-component");
                this.chartDatasets = [{data: data.isa, label:"isa"}];
                this.chartLabels.push(''); 
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
            pointHoverBorderColor: 'rgba(151,187,205,1)',
            radius: 0
        }
    ];

    public chartOptions:any = { 
        responsive: true,
        scales: {
            yAxes: [{
                stacked: false
            }]
        }
    };

    public chartClicked(e: any): void { 
            
    } 
    
    public chartHovered(e: any): void { 
            
    }
}