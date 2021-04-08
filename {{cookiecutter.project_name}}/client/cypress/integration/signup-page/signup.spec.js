/// <reference types="cypress" />
context('Signup Page', () => {
  beforeEach(() => {
    cy.visit(Cypress.env('baseUrl'))
  })

  // Before typing
  it('input should have base styles', () => {
    cy.get('[data-cy=signup-email]').should(
      'have.css',
      'border',
      '3px solid rgb(51, 51, 51)',
    )
  })

  it('.type() - type into a input element', () => {
    // https://on.cypress.io/type
    cy.get('[data-cy=signup-email]')
      .type('fake@email.com')
      .should('have.value', 'fake@email.com')

      // .type() with special character sequences
      .type('{leftarrow}{rightarrow}{uparrow}{downarrow}')
      .type('{del}{selectall}{backspace}')

      // .type() with key modifiers
      .type('{alt}{option}') //these are equivalent
      .type('{ctrl}{control}') //these are equivalent
      .type('{meta}{command}{cmd}') //these are equivalent
      .type('{shift}')
  })
})
