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
import { MChartComponent} from './components/card/mchart-component/mchart.component'
import {OverallComponent} from './components/cards/overall-component/overall.component'
import {ShortGraphComponent} from './components/cards/short-graph-component/short-graph.component'
import {LongGraphComponent} from './components/cards/long-graph-component/long-graph.component'
import {HistogramComponent} from './components/cards/histogram-component/histogram.component'
import {StreamComponent} from './components/cards/stream-component/stream.component'
import {QuteComponent} from './components/cards/qute-component/qute.component'

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
    ChartComponent,
    MChartComponent,
    OverallComponent,
    ShortGraphComponent,
    LongGraphComponent,
    HistogramComponent,
    StreamComponent,
    QuteComponent
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
