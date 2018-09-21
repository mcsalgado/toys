using System;
using System.Windows.Forms;

namespace BadAkinatorThing
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void startQueryButton_Click(object sender, EventArgs e)
        {
            Program.PlayGame();
        }
    }
}
