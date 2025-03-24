import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-dia',
  imports: [CommonModule],
  templateUrl: './dia.component.html',
  styleUrls: ['./dia.component.css']
})
export class DiaComponent implements OnInit {
  diaDatos: any;
  error: any;

  constructor(private http: HttpClient){}

  ngOnInit(): void {
    this.http.get('http://localhost:5000/vuelos/dia').subscribe(
      (data) => {
        this.diaDatos = data;
        console.log('Datos recibidos: ', this.diaDatos);
      },
      (error) => {
        this.error = 'Error en la petición: ' + error.message;
        console.error(this.error);
      }
      );
  }
}