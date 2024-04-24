% Define the function to be integrated
fun = @(x,t) x.^(t-1) .* exp(-x);

% Values of t to evaluate
values_of_t = [2, 4, 6, 8, 10];

% Lower and upper limits of integration
lower_limit = 0;
upper_limit = 10; % Same interval as used in part (a)

% Initialize arrays to store results and number of function evaluations
quad_results = zeros(size(values_of_t));
num_eval_quad = zeros(size(values_of_t));
trapezoidal_results = zeros(size(values_of_t));
num_eval_trapezoidal = zeros(size(values_of_t));

% Compute results using quad and trapezoidal rule
for i = 1:length(values_of_t)
    t = values_of_t(i);
    
    % Compute using quad
    tic;
    [quad_results(i),~,~,num_eval_quad(i)] = quad(@(x) fun(x,t), lower_limit, upper_limit);
    quad_time = toc;
    
    % Compute using trapezoidal rule
    tic;
    trapezoidal_results(i) = gamma_function_trapezoidal(t, lower_limit, upper_limit, num_subintervals);
    trapezoidal_time = toc;
    num_eval_trapezoidal(i) = num_subintervals + 1; % Number of function evaluations = number of intervals + 1
    
    % Display results
    fprintf('t = %d:\n', t);
    fprintf('Using quad:\n');
    fprintf('Result: %.8f\n', quad_results(i));
    fprintf('Number of function evaluations: %d\n', num_eval_quad(i));
    fprintf('Time taken: %.4f seconds\n', quad_time);
    fprintf('Using trapezoidal rule:\n');
    fprintf('Result: %.8f\n', trapezoidal_results(i));
    fprintf('Number of function evaluations: %d\n', num_eval_trapezoidal(i));
    fprintf('Time taken: %.4f seconds\n', trapezoidal_time);
    fprintf('\n');
end
