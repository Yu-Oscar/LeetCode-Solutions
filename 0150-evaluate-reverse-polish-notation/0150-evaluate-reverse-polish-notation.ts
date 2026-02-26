function evalRPN(tokens: string[]): number {
    const set = new Set(['+', '-', '*', '/'])
    let stack = []
    let ans = 0

    for (const token of tokens) {
        if (!set.has(token)) {
            stack.push(Number(token))
        } else {
            let b = stack.pop()
            let a = stack.pop()
            
            if (token == "+") stack.push(a+b)
            if (token == "-") stack.push(a-b)
            if (token == "*") stack.push(a*b)
            if (token == "/") stack.push(Math.trunc(a/b))
        }
    }

    return stack[0]
};