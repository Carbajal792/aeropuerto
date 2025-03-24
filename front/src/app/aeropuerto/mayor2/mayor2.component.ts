import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';

@Component({
  selector: 'app-mayor2',
  imports: [CommonModule],
  templateUrl: './mayor2.component.html',
  styleUrl: './mayor2.component.css'
})
export class Mayor2Component {
  mayores: any;
  error: any;

  constructor(private http: HttpClient){}

  ngOnInit(): void {
    this.http.get('http://localhost:5000/vuelos/mayor2').subscribe(
      (data) =>{
        this.mayores = data;
        console.log('Datos recibidos:' + this.mayores);
      },
      (error) => {
        this.error = error;
        console.error('Error en la petición: '+ error.message);
      }
    );
  }
}
