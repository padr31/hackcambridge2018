import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../../services/api.service';
import { Subscription } from 'rxjs/Subscription';


@Component({
    selector: 'overall-component',
    templateUrl: 'overall.component.html'
})


export class OverallComponent implements OnInit {

    processSubscription:Subscription;    
    apiService:ApiService;

    status:string;
    status_color:string = "#000000";


    constructor(apiService:ApiService) {
        this.apiService = apiService;
     }

    ngOnInit() { 
        this.processSubscription = this.apiService.imageChange.subscribe(
            data => {
                this.status = data.status;
                this.status_color = data.status_color;
            }
        );
    }
}