clc
clear
close all

%% Unweighted
M = [1 0;1 1;1 2;1 3];
y = [1;4;2;6];

a_unweighted = inv(M'*M) * (M' * y) 

%% Weighted
D = diag([1,2,3,sqrt(6)]);

a_weighted = inv(M'*D*M) * (M'*D*y)