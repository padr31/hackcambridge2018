import { BrowserModule } from '@angular/platform-browser';
import { NgModule, NO_ERRORS_SCHEMA } from '@angular/core';
import { MDBBootstrapModule } from 'angular-bootstrap-md';

import { AppComponent } from './app.component';
import { CardComponent} from './components/card/card.component'
import { ImageComponent} from './components/card/image-component/image.component'
import { NavbarComponent} from './components/navbar/navbar.component'


@NgModule({
  declarations: [
    AppComponent,
    CardComponent,
    ImageComponent,
    NavbarComponent
  ],
  imports: [
    BrowserModule,
    MDBBootstrapModule.forRoot()
  ],
  providers: [],
  bootstrap: [AppComponent],
  schemas: [ NO_ERRORS_SCHEMA ]
})
export class AppModule { }
