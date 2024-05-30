function pascalTriangle(n) {
    if (n <= 0) return [];

    const triangle = [[1]];

    for (let i = 1; i < n; i++) {
        const prevRow = triangle[triangle.length - 1];
        const newRow = [1];

        for (let j = 1; j < i; j++) {
            newRow.push(prevRow[j - 1] + prevRow[j]);
        }

        newRow.push(1);
        triangle.push(newRow);
    }

    return triangle;
}
