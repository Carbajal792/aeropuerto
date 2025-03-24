import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
@Component({
  selector: 'app-vuelos',
  imports: [CommonModule],
  templateUrl: './vuelos.component.html',
  styleUrl: './vuelos.component.css'
})
export class VuelosComponent {
  vuelosDatos: any;
  error: any;

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.http.get('http://localhost:5000/vuelos/masVuelos').subscribe(
      (data) => {
        this.vuelosDatos = data;
        console.log('Datos recibidos:', this.vuelosDatos);
      },
      (error) => {
        this.error = 'Error en la petición: ' + error.message;
        console.error(this.error);
      }
    );
  }
}
