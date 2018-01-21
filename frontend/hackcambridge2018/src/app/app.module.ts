import { BrowserModule } from '@angular/platform-browser';
import { NgModule, NO_ERRORS_SCHEMA } from '@angular/core';
import { MDBBootstrapModule } from 'angular-bootstrap-md';
import {HttpClientModule} from '@angular/common/http';


import { AppComponent } from './app.component';
import { CardComponent} from './components/card/card.component'
import { ImageComponent} from './components/card/image-component/image.component'
import { NavbarComponent} from './components/navbar/navbar.component'
import { GraphComponent} from './components/card/graph-component/graph.component'
import { SuggestionComponent} from './components/card/suggestion-component/suggestion.component'
import { ChartComponent} from './components/card/chart-component/chart.component'
//services
import {ApiService} from './services/api.service'

//modules
import { ChartsModule } from 'ng2-charts';


@NgModule({
  declarations: [
    AppComponent,
    CardComponent,
    ImageComponent,
    NavbarComponent,
    GraphComponent,
    SuggestionComponent,
    ChartComponent
  ],
  imports: [
    BrowserModule,
    MDBBootstrapModule.forRoot(),
    HttpClientModule,
    ChartsModule
  ],
  providers: [ApiService],
  bootstrap: [AppComponent],
  schemas: [ NO_ERRORS_SCHEMA ]
})
export class AppModule { }
