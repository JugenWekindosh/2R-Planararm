#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

typedef struct
{
    double x, y;
} Point2D;

Point2D evalOA(double theta1, double l1)
{
    Point2D A;
    A.x = l1 * cos(theta1);
    A.y = l1 * sin(theta1);
    return A;
}

Point2D evalAP(double theta1, double theta2, double l2)
{
    Point2D B;
    B.x = l2 * cos(theta1 + theta2);
    B.y = l2 * sin(theta1 + theta2);
    return B;
}

Point2D evalOP(Point2D A, Point2D B)
{
    Point2D P;
    P.x = A.x + B.x;
    P.y = A.y + B.y;
    return P;
}

void evalKinematic(const char *fname, double L1, double L2, double maxTheta, double thetaIncr)
{
    double Theta1, Theta2;
    Point2D OA, AP, OP;
    FILE *f = fopen(fname, "w");
    if (!f)
    {
        perror("Errore apertura file:");
        printf("%s\n", fname);
        exit(1);
    }

    for (double theta = 0.0; theta <= maxTheta; theta += thetaIncr)
    {
        Theta1 = theta;
        Theta2 = theta;

        OA = evalOA(Theta1, L1);
        AP = evalAP(Theta1, Theta2, L2);
        OP = evalOP(OA, AP);
        fprintf(f, "%.6f %.6f %.6f %.6f %.6f %.6f\n",
                OA.x, OA.y, AP.x, AP.y, OP.x, OP.y);
    }
    fclose(f);
}

void evalKinematicConfiguration(const char *fname, double L1, double L2, double Theta1, double Theta2)
{
    Point2D OA, AP, OP;
    FILE *f = fopen(fname, "w");
    if (!f)
    {
        perror("Errore apertura file:");
        printf("%s\n", fname);
        exit(1);
    }

    OA = evalOA(Theta1, L1);
    AP = evalAP(Theta1, Theta2, L2);
    OP = evalOP(OA, AP);
    fprintf(f, "%.6f %.6f %.6f %.6f %.6f %.6f\n",
            OA.x, OA.y, AP.x, AP.y, OP.x, OP.y);
    fclose(f);
}

int main()
{
    double L1 = 5.0;
    double L2 = 3.0;
    double maxTheta = 2 * M_PI;
    double thetaIncr = 0.1;

    evalKinematic("traj_data.txt", L1, L2, maxTheta, thetaIncr);

    double Theta1 = 15.0 * (M_PI / 180);
    double Theta2 = 0.0;
    evalKinematicConfiguration("sing_max.txt", L1, L2, Theta1, Theta2);

    double THeta1 = 15.0 * (M_PI / 180);
    double THeta2 = M_PI;
    evalKinematicConfiguration("sing_min.txt", L1, L2, THeta1, THeta2);

    printf("Esecuzione completata!\n");
    return 0;
}