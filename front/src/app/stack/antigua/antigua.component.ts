import { Component} from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-antigua',
  imports: [CommonModule],
  templateUrl: './antigua.component.html',
  styleUrl: './antigua.component.css'
})

export class AntiguaComponent {
    antiguaData: any;
    error: any;
    
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