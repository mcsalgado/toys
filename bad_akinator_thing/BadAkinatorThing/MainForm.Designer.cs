namespace BadAkinatorThing
{
    partial class MainForm
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.queryLabel = new System.Windows.Forms.Label();
            this.startQueryButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            //
            // queryLabel
            //
            this.queryLabel.AutoSize = true;
            this.queryLabel.Location = new System.Drawing.Point(51, 18);
            this.queryLabel.Name = "queryLabel";
            this.queryLabel.Size = new System.Drawing.Size(148, 13);
            this.queryLabel.TabIndex = 0;
            this.queryLabel.Text = "Think about a person.\nI will try to guess who it is!";
            //
            // startQueryButton
            //
            this.startQueryButton.Location = new System.Drawing.Point(83, 45);
            this.startQueryButton.Name = "startQueryButton";
            this.startQueryButton.Size = new System.Drawing.Size(75, 23);
            this.startQueryButton.TabIndex = 1;
            this.startQueryButton.Text = "OK";
            this.startQueryButton.UseVisualStyleBackColor = true;
            this.startQueryButton.Click += new System.EventHandler(this.startQueryButton_Click);
            //
            // MainForm
            //
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(243, 80);
            this.Controls.Add(this.startQueryButton);
            this.Controls.Add(this.queryLabel);
            this.Name = "MainForm";
            this.Text = "Bad Akinator Thing: The Game";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Label queryLabel;
        private System.Windows.Forms.Button startQueryButton;
    }
}
