import { TestBed } from '@angular/core/testing';

import { AntiguaService } from './antigua.service';

describe('AntiguaService', () => {
  let service: AntiguaService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(AntiguaService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
