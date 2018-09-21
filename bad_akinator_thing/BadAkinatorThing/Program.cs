using System;
using System.Windows.Forms;

namespace BadAkinatorThing
{
    static class Program
    {
        private static CategoryChain root;

        private static void InitializeSampleCategoryChain()
        {
            root = new CategoryChain(complementMember: "D. Pedro I");
            root.AddCategory(categoryName: "a boxer", complementMember: "Muhammad Ali");
        }

        public static void PlayGame()
        {
            var currentCategoryChain = root;
            while (currentCategoryChain != null)
            {
                currentCategoryChain = Query(currentCategoryChain);
            }
        }

        private static CategoryChain Query(CategoryChain categoryChain)
        {
            const string guessMessage = "Is this person {0}?";

            var currentNode = categoryChain.head;
            while (currentNode != null)
            {
                if (MessageBox.Show(String.Format(guessMessage, currentNode.name), "Confirm", MessageBoxButtons.YesNo, MessageBoxIcon.Question) == DialogResult.Yes)
                {
                    return currentNode.inside;
                }
                currentNode = currentNode.next;
            }


            if (MessageBox.Show(String.Format(guessMessage, categoryChain.complementMember), "Confirm", MessageBoxButtons.YesNo, MessageBoxIcon.Question) == DialogResult.Yes)
            {
                MessageBox.Show("Great, guessed right one more time!", "Bad Akinator Thing", MessageBoxButtons.OK, MessageBoxIcon.Information);
                return null;
            }

            var newElement = "";
            while (newElement == "")
            {
                newElement = Microsoft.VisualBasic.Interaction.InputBox("Bravo, you have defeated me! Who are you thinking about?", "I give up", "");
            }

            var newCategoryName = "";
            while (newCategoryName == "")
            {
                newCategoryName = Microsoft.VisualBasic.Interaction.InputBox($"{newElement} is _____ but {categoryChain.complementMember} is not.", "Complete", "");
            }

            categoryChain.AddCategory(newCategoryName, newElement);

            return null;
        }


        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            InitializeSampleCategoryChain();
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new MainForm());
        }
    }
}
