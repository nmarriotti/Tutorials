#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QFileDialog>
#include <QFile>
#include <QTextStream>
#include <QMessageBox>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    this->setCentralWidget(ui->textEdit);
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_actionOpen_triggered()
{
    QString filename = QFileDialog::getOpenFileName(  // open file dialog
                this,
                tr("Open File"),
                "/",
                "All files (*.*);;Text file (*.txt)"
    );
    QFile file(filename);  // create file object
    if(!file.open(QIODevice::ReadOnly)) {
        QMessageBox::information(0,"Info",file.errorString());
    } else {
        QTextStream in(&file); // set text stream
        ui->textEdit->setText(in.readAll());  // show file contents in textEdit widget
        //this->setWindowTitle(filename);  // update window title
        this->statusBar()->showMessage(filename);
    }
}

void MainWindow::on_actionSave_triggered()
{
    QString filename = QFileDialog::getSaveFileName(this,"Save File","/","All files (*.*);;Text file (*.txt)");
    QFile file(filename);
    if(!file.open(QIODevice::WriteOnly)) {
        QMessageBox::information(0,"Info",file.errorString());
    } else {
        QTextStream out(&file);
        out << ui->textEdit->toPlainText();
        QMessageBox::information(0,"Info","File saved!");
    }
}
