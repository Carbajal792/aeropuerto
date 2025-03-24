import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
@Injectable({
  providedIn: 'root'
})
export class ReputacionService {
  private apiUrl = 'http://127.0.0.1:5000/stack/reputacion';
  constructor(private http: HttpClient) { }

  getReputation(): Observable<any> {
    return this.http.get(this.apiUrl);
  }
}
