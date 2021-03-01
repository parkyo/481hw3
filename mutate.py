import sys, ast, astor, random, pprint

#random.seed( 5000 )

class myVisitor( ast.NodeVisitor ):
    def __init__ (self):
        self.counter = 0

    def visit_BinOp( self, node ):
        if isinstance(node.op, ast.Add):
            self.counter += 1
            print('Visiting Add, counter = {}'.format(self.counter))

        return self.generic_visit(node) # continue visiting the rest

# mutate the random node
class myTransformer(ast.NodeTransformer):
    def __init__(self, nodeToMutate):
        self.counter = 0
        self.nodeToMutate = nodeToMutate

    def visit_BinOp(self, node):
        if isinstance(node.op, ast.Add):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.BinOp()
                new_node.left = node.left
                new_node.right = node.right

                new_node.op = ast.Sub()

                print('changing add {} to sub.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging
        
        if isinstance(node.op, ast.Sub):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.BinOp()
                new_node.left = node.left
                new_node.right = node.right

                new_node.op = ast.Add()

                print('changing sub {} to add.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging
        
        if isinstance(node.op, ast.FloorDiv):
           self.counter += 1

           if self.counter == self.nodeToMutate:
               new_node = ast.BinOp()
               new_node.left = node.left
               new_node.right = node.right

               new_node.op = ast.Div()

               print('changing floorDiv {} to div.'.format(self.counter))
               return ast.copy_location(new_node, node) # helps debugging
               
        if isinstance(node.op, ast.Div):
           self.counter += 1

           if self.counter == self.nodeToMutate:
               new_node = ast.BinOp()
               new_node.left = node.left
               new_node.right = node.right

               new_node.op = ast.FloorDiv()

               print('changing div {} to floordiv.'.format(self.counter))
               return ast.copy_location(new_node, node) # helps debugging
               
        
        if isinstance(node.op, ast.Mult):
           self.counter += 1

           if self.counter == self.nodeToMutate:
               new_node = ast.BinOp()
               new_node.left = node.left
               new_node.right = node.right

               new_node.op = ast.Pow()

               print('changing mult {} to pow.'.format(self.counter))
               return ast.copy_location(new_node, node) # helps debugging

        return self.generic_visit(node)
        
        
    def visit_Compare(self, node):
        if isinstance(node.op, ast.LtE):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.Compare()
                new_node.left = node.left
                new_node.right = node.right

                new_node.op = ast.Gt()

                print('changing lessThanEqual {} to greaterThan.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging
        
        if isinstance(node.op, ast.GtE):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.Compare()
                new_node.left = node.left
                new_node.right = node.right

                new_node.op = ast.Lt()

                print('changing GTE {} to LT.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging

        if isinstance(node.op, ast.Gt):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.Compare()
                new_node.left = node.left
                new_node.right = node.right

                new_node.op = ast.LtE()

                print('changing GT {} to LtE.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging

        if isinstance(node.op, ast.Lt):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.Compare()
                new_node.left = node.left
                new_node.right = node.right

                new_node.op = ast.GtE()

                print('changing LT {} to GtE.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging

        if isinstance(node.op, ast.Eq):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.Compare()
                new_node.left = node.left
                new_node.right = node.right

                new_node.op = ast.NotEq()

                print('changing eq {} to neq.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging
                
        
        if isinstance(node.op, ast.NotEq):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.Compare()
                new_node.left = node.left
                new_node.right = node.right

                new_node.op = ast.Eq()

                print('changing neq {} to eq.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging


        if isinstance(node.op, ast.Is):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.Compare()
                new_node.left = node.left
                new_node.right = node.right

                new_node.op = ast.IsNot()

                print('changing is {} to isnot.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging
                
                
        if isinstance(node.op, ast.IsNot):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.Compare()
                new_node.left = node.left
                new_node.right = node.right

                new_node.op = ast.Is()

                print('changing isnot {} to is.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging
                
                
        if isinstance(node.op, ast.In):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.Compare()
                new_node.left = node.left
                new_node.right = node.right

                new_node.op = ast.NotIn()

                print('changing In {} to InNot.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging
                
                
        if isinstance(node.op, ast.NotIn):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.Compare()
                new_node.left = node.left
                new_node.right = node.right

                new_node.op = ast.In()

                print('changing Notin {} to in.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging

        return self.generic_visit(node)
        
    
    def visit_BoolOp(self, node):
        if isinstance(node.op, ast.And):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.BoolOp()
                new_node.left = node.left
                new_node.right = node.right

                new_node.op = ast.Or()

                print('changing and {} to or.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging
                
        if isinstance(node.op, ast.Or):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.BoolOp()
                new_node.left = node.left
                new_node.right = node.right

                new_node.op = ast.And()

                print('changing or {} to and.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging
                    
                    
    def visit_Assign(self, node):
        if isinstance(node.op, ast.Assign(targets=[ast.Name(id='q1', ctx=ast.Store()),], value=ast.Name(id='s1',ctx=ast.Load()))):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                (node.left).right = node.right
                (node.right).left = node.left

                print('deleting assignment for {}'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging
                
        return self.generic_visit(node)



my_tree = None
with open(sys.argv[1]) as f:
    source = f.read()
    my_tree = ast.parse( source )

my_visited_tree = myVisitor()
my_visited_tree.visit(my_tree)

for i in range(sys.argv[2]):
    node_to_mutate = random.randint(1, my_visited_tree.counter)

    my_transformed_node = myTransformer(node_to_mutate)
    my_transformed_node.visit(my_tree)

# deepcopy and save with the formatted names
print(astor.to_source(my_tree))
