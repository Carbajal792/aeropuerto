import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-movimiento',
  imports: [CommonModule],
  templateUrl: './movimiento.component.html',
  styleUrls: ['./movimiento.component.css']
})
export class MovimientoComponent implements OnInit {
  movDatos: any;
  error: any;

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.http.get('http://localhost:5000/vuelos/masMovimiento').subscribe(
      (data) => {
        this.movDatos = data;
        console.log('Datos recibidos:', this.movDatos);
      },
      (error) => {
        this.error = 'Error en la petición: ' + error.message;
        console.error(this.error);
      }
    );
  }
}
