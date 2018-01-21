import { Component } from '@angular/core';

@Component({
 selector: 'chart-component',
 templateUrl: './chart.component.html'
})
export class ChartComponent {
 // lineChart
 public lineChartData:Array<any> = [
   {data: [65, 59, 80, 81, 56, 55, 40], label: 'Series A'},
 ];
 public lineChartLabels:Array<any> = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];
 public lineChartOptions:any = {
   responsive: true
 };
 public lineChartColors:Array<any> = [
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
 public lineChartLegend:boolean = true;
 public lineChartType:string = 'line';

 // events
 public chartClicked(e:any):void {
   console.log(e);
 }

 public chartHovered(e:any):void {
   console.log(e);
 }
}