import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app.component';
import { provideHttpClient } from '@angular/common/http';
import { MovimientoComponent } from './app/aeropuerto/movimiento/movimiento.component';
import { VuelosComponent } from './app/aeropuerto/vuelos/vuelos.component';
import { DiaComponent } from './app/aeropuerto/dia/dia.component';
import { Mayor2Component } from './app/aeropuerto/mayor2/mayor2.component';
import { ContarComponent } from './app/stack/contar/contar.component';
import { ReputacionComponent } from './app/stack/reputacion/reputacion.component';
import { VistasComponent } from './app/stack/vistas/vistas.component';
import { AntiguaComponent } from './app/stack/antigua/antigua.component';

bootstrapApplication(AppComponent, appConfig)
  .catch((err) => console.error(err));

  
bootstrapApplication(MovimientoComponent, {
  providers: [provideHttpClient()]
}).catch((err) => console.error(err));
  

bootstrapApplication(VuelosComponent, {
  providers: [provideHttpClient()]
}).catch((err) => console.error(err));

bootstrapApplication(DiaComponent, {
  providers: [provideHttpClient()]
}).catch((err) => console.error(err));

bootstrapApplication(Mayor2Component, {
  providers: [provideHttpClient()]
}).catch((err) => console.error(err));

bootstrapApplication(ContarComponent, {
  providers: [provideHttpClient()]
}).catch((err) => console.error(err));

bootstrapApplication(ReputacionComponent, {
  providers: [provideHttpClient()]
}).catch((err) => console.error(err));

bootstrapApplication(VistasComponent, {
  providers: [provideHttpClient()]
}).catch((err) => console.error(err));

bootstrapApplication(AntiguaComponent, {
  providers: [provideHttpClient()]
}).catch((err) => console.error(err));