data=load('C:\Users\Arnab Maji\Desktop\MLP\email-Eu-core.txt');
source=data(:,1);
target=data(:,2);
nodes=union(source,target);
edge = [data(:,1),data(:,2)];
%Adjacency Matrix

AdjMat = zeros(length(nodes),length(nodes));

for i = 1:length(nodes)
    row = bsearch(nodes,edge(i,1),0,length(nodes));
    column = bsearch(nodes,edge(i,2),0,length(nodes));
    if row < 286 && column < 286
        A(row,column) = 1;
    end
end

% we have the adjacency matrix