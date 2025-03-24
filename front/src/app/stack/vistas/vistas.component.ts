import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-vistas',
  imports: [CommonModule],
  templateUrl: './vistas.component.html',
  styleUrl: './vistas.component.css'
})
export class VistasComponent {
  vistasData: any;
  error: any;
  constructor(private http:HttpClient){}
  ngOnInit(): void {
    this.http.get('http://localhost:5000/stack/vistas').subscribe(
      (data) => {
        this.vistasData = data;
        console.log('Datos recibidos: ', this.vistasData);
      },
      (error) => {
        this.error = error;
        console.error('Error en la petición: ' + error.message);
      }
    );
  }
}
