import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class VistasService {
  private apiUrl = 'http://127.0.0.1:5000/stack/vistas'; // Ajusta la URL de tu API

  constructor(private http: HttpClient) { }

  getReputation(): Observable<any> {
    return this.http.get(this.apiUrl);
  }
}
