import { Component} from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
@Component({
  selector: 'app-contar',
  imports: [CommonModule],
  templateUrl: './contar.component.html',
  styleUrl: './contar.component.css'
})
export class ContarComponent {
  contarData: any;
  error: any;

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
