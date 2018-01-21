import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../../services/api.service';
import { Subscription } from 'rxjs/Subscription';

@Component({
    selector: 'qute-component',
    templateUrl: 'qute.component.html'
})

export class QuteComponent implements OnInit {
 
    apiService:ApiService;
    processSubscription:Subscription;        

    constructor(apiService:ApiService) { 
        this.apiService = apiService;
    }

    ngOnInit() { 
        this.processSubscription = this.apiService.imageChange.subscribe(
            data => {
                this.suggestion = data.suggestion;
            }
        );

    }
}