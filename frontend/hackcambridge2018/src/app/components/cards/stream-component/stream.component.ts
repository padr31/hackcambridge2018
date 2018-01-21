import { Component, OnInit, OnDestroy } from '@angular/core';
import {ApiService} from './../../../services/api.service'
import { Subscription } from 'rxjs/Subscription';

@Component({
    selector: 'stream-component',
    templateUrl: 'stream.component.html'
})

export class StreamComponent implements OnInit, OnDestroy {

    defaultImageUrl = "http://172.20.1.132:5000/last_image.jpg";
    imageUrl:string = "http://172.20.1.132:5000/last_image.jpg";
    apiService:ApiService;
    processSubscription:Subscription;
    counter:number = 0;

    constructor(apiService: ApiService) {
        this.apiService = apiService;
    }

    ngOnInit() { 
        this.processSubscription = this.apiService.imageChange.subscribe(
            data => {
                //console.log("Got data in image-component");
                //console.log(data);
                this.imageUrl = this.defaultImageUrl + "?t=" + new Date().getTime();
            }
        );
    }

    ngOnDestroy() {
        this.processSubscription.unsubscribe();
    }
}