import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'suggestion-component',
    template: `
    <h1>{{suggestion}}</h1>
    `
})

export class SuggestionComponent implements OnInit {
    
    suggestion:string;

    constructor() { 
        this.suggestion = "Say a Joke."
    }

    ngOnInit() { }
}