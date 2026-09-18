import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class DashboardService {

  private apiUrl = 'https://contractiq-backend-0jnq.onrender.com/reports/dashboard';

  constructor(private http: HttpClient) {}

  getDashboardSummary() {
    return this.http.get<any>(
      `${this.apiUrl}/summary`
    );
  }
}