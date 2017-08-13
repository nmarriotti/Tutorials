#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <QMessageBox>
#include <thread>
#include <chrono>

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    ui->pushButton->setToolTip("This is a tooltip");
    connect(ui->horizontalSlider,SIGNAL(valueChanged(int)),ui->progressBar,SLOT(setValue(int)));
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_clicked()
{
    ui->label->setText("You clicked the button!");
}

void MainWindow::on_pushButton_2_clicked()
{
    QMessageBox::about(this, "Title", "This is a message box!");
}

void MainWindow::on_pushButton_3_clicked()
{
    QMessageBox::StandardButton quitBtn = QMessageBox::question(this, "Title", "Quit Program?",QMessageBox::Yes | QMessageBox::No);

    if(quitBtn == QMessageBox::Yes) {
        QApplication::quit();
    } else {
        ui->label->setText("You chose No.");
        qDebug("You chose No");
    }
}

void MainWindow::on_pushButton_4_clicked()
{
    for(int i=0; i<ui->progressBar->maximum(); i++) {
        ui->progressBar->setValue(i);
    }
}
