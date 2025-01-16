describe('Admin Login', () => {
  const username = 'app'; // Valid username
  const password = 'Skoda1$$'; // Valid password

  it('should log in with valid credentials and redirect to admin panel', () => {
    // Visit the admin login page
    cy.visit('http://test.aquitas.dynv6.net:28080/admin/login/?next=/admin/');

    // Type the username and password into the respective fields
    cy.get('input[name="username"]').type(username); // Select username input field and type valid username
    cy.get('input[name="password"]').type(password); // Select password input field and type valid password

    // Submit the login form
    cy.get('form').submit();

    // Assert that the user is redirected to the admin dashboard ("/admin/")
    cy.url().should('include', '/admin/'); // URL should contain "/admin/"
    cy.get('h1').should('contain', 'Site administration'); // Check that the page contains the admin heading
  });

  it('should show an error with invalid credentials', () => {
    // Visit the login page again
    cy.visit('http://test.aquitas.dynv6.net:28080/admin/login/?next=/admin/');

    // Type invalid credentials
    cy.get('input[name="username"]').type('invalid_user'); // Use incorrect username
    cy.get('input[name="password"]').type('wrongpassword'); // Use incorrect password

    // Submit the login form
    cy.get('form').submit();

    // Assert that an error message is displayed
    cy.get('.login-error').should('contain', 'Please enter the correct username and password.');
    cy.url().should('include', '/admin/login/'); // URL should remain on the login page
  });
});