import { TestBed } from '@angular/core/testing';

import { ReputacionService } from './reputacion.service';

describe('ReputacionService', () => {
  let service: ReputacionService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ReputacionService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
