import { Component } from '@angular/core';
import { AntiguaComponent } from './stack/antigua/antigua.component';
import { ContarComponent } from './stack/contar/contar.component';
import { ReputacionComponent } from './stack/reputacion/reputacion.component';
import { VistasComponent } from './stack/vistas/vistas.component';
import { DiaComponent } from './aeropuerto/dia/dia.component';
import { Mayor2Component } from './aeropuerto/mayor2/mayor2.component';
import { MovimientoComponent } from './aeropuerto/movimiento/movimiento.component';
import { VuelosComponent } from './aeropuerto/vuelos/vuelos.component';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone:true,
  imports: [CommonModule,FormsModule,AntiguaComponent,ContarComponent,ReputacionComponent,VistasComponent,DiaComponent,Mayor2Component,MovimientoComponent,VuelosComponent],
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent{
  selectedOption: String = "antigua";
}