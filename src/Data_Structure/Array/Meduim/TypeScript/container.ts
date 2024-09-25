const maxArea = (height: number[]): number => {
    let left: number = 0;
    let right: number = height.length - 1;
    let maxArea: number = 0;

    while (left < right) {
        const distance: number = right - left;
        const currentArea: number = Math.min(height[left], height[right]) * distance;

        maxArea = Math.max(maxArea, currentArea);

        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }

    return maxArea;
};

const height: number[] = [1, 8, 6, 2, 5, 4, 8, 3, 7];
const result: number = maxArea(height);
console.log(result);  
