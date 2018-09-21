namespace BadAkinatorThing
{
    class CategoryNode
    {
        public string name;
        public CategoryChain inside;
        public CategoryNode next;

        public CategoryNode(string name)
        {
            this.name = name;
        }
    }

    class CategoryChain
    {
        public CategoryNode head;

        // NOTE(mcsalgado): a complementMember is a member of the category but
        // is NOT a member of any of the category nodes contained in the chain
        public string complementMember;

        public CategoryChain(string complementMember)
        {
            this.complementMember = complementMember;
        }

        /// <summary>
        /// Adds a new category to the end of the chain
        /// </summary>
        public void AddCategory(string categoryName, string complementMember)
        {
            var newNode = new CategoryNode(categoryName);
            newNode.inside = new CategoryChain(complementMember);

            if (head == null)
            {
                head = newNode;
                return;
            }

            var currentNode = head;
            while (currentNode.next != null)
            {
                currentNode = currentNode.next;
            }
            currentNode.next = newNode;
        }
    }
}
