import sys, ast, astor, random, pprint

#random.seed( 5000 )

class myVisitor( ast.NodeVisitor ):
    def __init__ (self):
        self.counter = 0

    def visit_BinOp( self, node ):
        if isinstance(node.op, ast.Add):
            self.counter += 1
            print('Visiting Add, counter = {}'.format(self.counter))
            
        if isinstance(node.op, ast.Sub):
            self.counter += 1
            print('Visiting sub, counter = {}'.format(self.counter))

        if isinstance(node.op, ast.Mult):
            self.counter += 1
            print('Visiting mult, counter = {}'.format(self.counter))

        if isinstance(node.op, ast.FloorDiv):
            self.counter += 1
            print('Visiting Floordiv, counter = {}'.format(self.counter))

        if isinstance(node.op, ast.Div):
            self.counter += 1
            print('Visiting Div, counter = {}'.format(self.counter))
#
        return self.generic_visit(node) # continue visiting the rest
        
        
    def visit_Compare( self, node ):
        if isinstance(node.ops, ast.GtE):
            self.counter += 1
            print('Visiting Gte, counter = {}'.format(self.counter))

        if isinstance(node.ops, ast.Gt):
            self.counter += 1
            print('Visiting Gt, counter = {}'.format(self.counter))

        if isinstance(node.ops, ast.LtE):
            self.counter += 1
            print('Visiting lte, counter = {}'.format(self.counter))

        if isinstance(node.ops, ast.Lt):
            self.counter += 1
            print('Visiting lt, counter = {}'.format(self.counter))


        return self.generic_visit(node) # continue visiting the rest

    def visit_BoolOp( self, node ):
        if isinstance(node.op, ast.And):
            self.counter += 1
            print('Visiting , counter = {}'.format(self.counter))

        return self.generic_visit(node) # continue visiting the rest

    def visit_Assign( self, node ):
        if isinstance(node, ast.Assign):
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
                if node.left is not None:
                    new_node.left = node.left

                if node.right is not None:
                    new_node.right = node.right

                new_node.ops = [ast.Sub()]

                print('changing add {} to sub.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging
        
        if isinstance(node.op, ast.Sub):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.BinOp()
                if node.left is not None:
                    new_node.left = node.left

                if node.right is not None:
                    new_node.right = node.right

                new_node.op = ast.Add()

                print('changing sub {} to add.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging
        
        if isinstance(node.op, ast.FloorDiv):
           self.counter += 1

           if self.counter == self.nodeToMutate:
               new_node = ast.BinOp()
                if node.left is not None:
                    new_node.left = node.left

                if node.right is not None:
                    new_node.right = node.right

               new_node.op = ast.Div()

               print('changing floorDiv {} to div.'.format(self.counter))
               return ast.copy_location(new_node, node) # helps debugging
               
        if isinstance(node.op, ast.Div):
           self.counter += 1

           if self.counter == self.nodeToMutate:
               new_node = ast.BinOp()
                if node.left is not None:
                    new_node.left = node.left

                if node.right is not None:
                    new_node.right = node.right

               new_node.op = ast.FloorDiv()

               print('changing div {} to floordiv.'.format(self.counter))
               return ast.copy_location(new_node, node) # helps debugging
               
        
        if isinstance(node.op, ast.Mult):
           self.counter += 1

           if self.counter == self.nodeToMutate:
               new_node = ast.BinOp()
                if node.left is not None:
                    new_node.left = node.left
                if node.right is not None:
                    new_node.right = node.right

               new_node.op = ast.Pow()

               print('changing mult {} to pow.'.format(self.counter))
               return ast.copy_location(new_node, node) # helps debugging

        return self.generic_visit(node)
        
        
    def visit_Compare(self, node):
        if isinstance(node.ops, ast.LtE):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.Compare()
                if node.left is not None:
                    new_node.left = node.left
                if node.right is not None:
                    new_node.right = node.right

                new_node.ops = [ast.Gt()]

                print('changing lessThanEqual {} to greaterThan.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging
        
        if isinstance(node.ops, ast.GtE):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.Compare()
                if node.left is not None:
                    new_node.left = node.left
                if node.right is not None:
                    new_node.right = node.right

                new_node.op = [ast.Lt()]

                print('changing GTE {} to LT.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging

        if isinstance(node.ops, ast.Gt):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.Compare()
                if node.left is not None:
                    new_node.left = node.left
                if node.right is not None:
                    new_node.right = node.right

                new_node.ops = [ast.LtE()]

                print('changing GT {} to LtE.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging

        if isinstance(node.ops, ast.Lt):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.Compare()
                if node.left is not None:
                    new_node.left = node.left
                if node.right is not None:
                    new_node.right = node.right

                new_node.ops = [ast.GtE()]

                print('changing LT {} to GtE.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging

        if isinstance(node.ops, ast.Eq):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.Compare()
                if node.left is not None:
                    new_node.left = node.left
                if node.right is not None:
                    new_node.right = node.right

                new_node.ops =[ ast.NotEq() ]

                print('changing eq {} to neq.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging
                
        
        if isinstance(node.ops, ast.NotEq):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.Compare()
                if node.left is not None:
                    new_node.left = node.left
                if node.right is not None:
                    new_node.right = node.right

                new_node.ops = ast.Eq()

                print('changing neq {} to eq.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging


        if isinstance(node.ops, ast.Is):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.Compare()
                if node.left is not None:
                    new_node.left = node.left
                if node.right is not None:
                    new_node.right = node.right

                new_node.ops = ast.IsNot()

                print('changing is {} to isnot.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging
                
                
        if isinstance(node.ops, ast.IsNot):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.Compare()
                if node.left is not None:
                    new_node.left = node.left
                if node.right is not None:
                    new_node.right = node.right

                new_node.ops = ast.Is()

                print('changing isnot {} to is.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging
                
                
        if isinstance(node.ops, ast.In):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.Compare()
                if node.left is not None:
                    new_node.left = node.left
                if node.right is not None:
                    new_node.right = node.right

                new_node.ops = ast.NotIn()

                print('changing In {} to InNot.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging
                
                
        if isinstance(node.ops, ast.NotIn):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.Compare()
                if node.left is not None:
                    new_node.left = node.left
                if node.right is not None:
                    new_node.right = node.right

                new_node.ops = ast.In()

                print('changing Notin {} to in.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging

        return self.generic_visit(node)
        
    
    def visit_BoolOp(self, node):
        if isinstance(node.op, ast.And):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.BoolOp()
                if node.left is not None:
                    new_node.left = node.left
                if node.right is not None:
                    new_node.right = node.right

                new_node.op = ast.Or()

                print('changing and {} to or.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging
                
        if isinstance(node.op, ast.Or):
            self.counter += 1

            if self.counter == self.nodeToMutate:
                new_node = ast.BoolOp()
                if node.left is not None:
                    new_node.left = node.left
                if node.right is not None:
                    new_node.right = node.right

                new_node.op = ast.And()

                print('changing or {} to and.'.format(self.counter))
                return ast.copy_location(new_node, node) # helps debugging
                    
        return self.generic_visit(node)

    def visit_Assign(self, node):
        if isinstance(node, ast.Assign):
            self.counter += 1

            if self.counter == self.nodeToMutate:

                print('deleting assignment for {}'.format(self.counter))
                return None # helps debugging
        return self.generic_visit(node)




my_tree = None
with open(sys.argv[1]) as f:
    source = f.read()
    my_tree = ast.parse( source )

for i in range(int(sys.argv[2])):
    my_visited_tree = myVisitor()
    my_visited_tree.visit(my_tree)
    
    node_to_mutate = random.randint(1, my_visited_tree.counter)

    my_transformed_node = myTransformer(node_to_mutate)
    my_transformed_node.visit(my_tree)

# deepcopy and save with the formatted names
print(astor.to_source(my_tree))
