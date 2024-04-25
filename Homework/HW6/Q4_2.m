% Define the function to be integrated
fun = @(x,t) x.^(t-1) .* exp(-x);

% Values of t to evaluate
values_of_t = [2, 4, 6, 8, 10];

% Lower and upper limits of integration
lower_limit = 0;
upper_limit = 10; % Same interval as used in part (a)

% Preallocate
quad_results = zeros(size(values_of_t));
num_eval_quad = zeros(size(values_of_t));
rel_err = zeros(size(values_of_t));

% Compute results using quad and trapezoidal rule
for i = 1:length(values_of_t)
    t = values_of_t(i);
    
    % Compute using quad
    %tic;
    [quad_results(i),num_eval_quad(i)] = quad(@(x) fun(x,t), lower_limit, upper_limit);
    rel_err(i) = abs(quad_results(i) - factorial(t-1)) / factorial(t-1);
    
    % Display results
    fprintf('t = %d:\n', t);
    %fprintf('Using quad:\n');
    fprintf('Result: %.8f\n', quad_results(i));
    fprintf('Number of function evaluations: %d\n', num_eval_quad(i));
    fprintf('Relative error: %.4f \n', rel_err(i));
    fprintf('\n');
end
