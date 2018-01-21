import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { ResponseContentType, RequestOptionsArgs } from '@angular/http';
import {DomSanitizer} from '@angular/platform-browser';
import 'rxjs/add/operator/map';
import { Subject } from 'rxjs/Subject';
import 'rxjs/add/observable/interval';
import { PResponse } from './response';

@Injectable()
export class ApiService {

    public imageChange: Subject<PResponse> = new Subject<PResponse>();
    imageLocation: string = "https://jsonplaceholder.typicode.com/photos/1";
    processLocation: string = "http://172.20.1.132:5000/process";

    constructor(private http: HttpClient) { 
        console.log("Subscribing");
        
        this.repeatProcess(this.processLocation);
    }
    

    getImage(imageUrl: string): Observable<string> {
        let headers = new HttpHeaders();
        headers.append('Access-Control-Allow-Origin','*');

        return this.http
            .get<string>(this.imageLocation, {headers: headers});    
    }

    process(processUrl:string): Observable<PResponse> {
        let headers = new HttpHeaders();
        headers.append('Access-Control-Allow-Origin','*');

        return this.http
            .get<PResponse>(processUrl, {headers: headers}); 
    }

    repeatProcess(processUrl:string) {
        let headers = new HttpHeaders();
        headers.append('Access-Control-Allow-Origin','*');

        this.http
        .get<PResponse>(processUrl, {headers: headers})
        .subscribe(
            data => {
            this.imageChange.next((data));
            //console.log("processed, going for another");
            this.repeatProcess(this.processLocation);
        }); 
    }

    /*getImageInInterval(imageUrl: string): Observable<string> {
        Observable.interval(3000)
        .flatMap(() => this.http.get(imageUrl)
        .map( res => res.json() )
        .catch( (error:any) => Observable.throw(error.json().error || 'Server error') ) )
        .subscribe(data => {
           console.log(data)
        })
    }*/
    
}