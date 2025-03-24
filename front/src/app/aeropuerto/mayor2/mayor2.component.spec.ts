import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Mayor2Component } from './mayor2.component';

describe('Mayor2Component', () => {
  let component: Mayor2Component;
  let fixture: ComponentFixture<Mayor2Component>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Mayor2Component]
    })
    .compileComponents();

    fixture = TestBed.createComponent(Mayor2Component);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
