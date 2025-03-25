import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-contar',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './contar.component.html',
  styleUrl: './contar.component.css'
})
export class ContarComponent implements OnInit{
  contarData: any;
  error: any;
  opcion:number=1;
  constructor(private http: HttpClient){}

  ngOnInit(): void {
    this.http.get('http://localhost:5000/stack/contar').subscribe(
      (data) =>{
        this.contarData = data;
        console.log('Datos recibidos:' + this.contarData);
      },
      (error) => {
        this.error = error;
        console.error('Error en la petición: '+ error.message);
      }
    );
  }
  }
