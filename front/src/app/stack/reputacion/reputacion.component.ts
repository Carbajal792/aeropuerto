import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-reputacion',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './reputacion.component.html',
  styleUrls: ['./reputacion.component.css']
})

export class ReputacionComponent implements OnInit{
  reputacionData: any;
  error: any;
  opcion:number =2;
  constructor(private http: HttpClient){}

  ngOnInit(): void {
    this.http.get('http://localhost:5000/stack/reputacion').subscribe(
      (data) =>{
        this.reputacionData = data;
        console.log('Datos recibidos: '+this.reputacionData);
      },
      (error) =>{
        this.error = error;
        console.error('Error en petición: ' +error.message);
      }
    );
  }
}
