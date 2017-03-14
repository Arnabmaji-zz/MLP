function [pos] = bsearch(arr,element,beg,endidx)
% assume that the array is ascending ordered

while(1)
    
    if endidx==beg
        pos=-1;
        return;
    end
    mid = floor((beg + endidx)/2);
    if(arr(mid) > element)
        pos = bsearch(arr,element,beg,mid);
        return;
    end
    if(arr(mid) < element)
        pos = bsearch(arr,element,mid,endidx);
        return;
    end
    if(arr(mid)==element)
        pos = mid;
        return;
    end
end
end