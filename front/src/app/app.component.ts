import { Component } from '@angular/core';
import { AntiguaComponent } from './stack/antigua/antigua.component';
import { VuelosComponent } from "./aeropuerto/vuelos/vuelos.component"; 
import { MovimientoComponent } from './aeropuerto/movimiento/movimiento.component';
import { Mayor2Component } from "./aeropuerto/mayor2/mayor2.component";

@Component({
  selector: 'app-root',
  imports: [Mayor2Component],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {

}