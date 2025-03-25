import { Component , OnInit} from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { ContarComponent } from "../contar/contar.component";
import { ReputacionComponent } from "../reputacion/reputacion.component";
import { VistasComponent } from "../vistas/vistas.component";

@Component({
  selector: 'app-antigua',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './antigua.component.html',
  styleUrl: './antigua.component.css'
})

export class AntiguaComponent implements OnInit {
    antiguaData: any;
    error: any;
    opcion:number=0;
    constructor(private http:HttpClient)  {}

    ngOnInit(): void{
      this.http.get('http://localhost:5000/stack/fecha').subscribe(
        (data) => {
          this.antiguaData = data;
          console.log('Datos recibidos: '+ this.antiguaData);
        },
        (error) => {
          this.error = error;
          console.error('Error en peticion: ' + this.error.message);
        }
      );
    }
}