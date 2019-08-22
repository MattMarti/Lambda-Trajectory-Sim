#include <vector>
#include "Eigen/Dense"

namespace Numerical_Methods {
    
    /*
    Cubic spline interpolation class
    Solves for the parameters that describe a cubic spline.To be used in
    conjunction with "cubicsplineInterp".This function can solve the
    parameters of a cubic spline given data from a vectorized system.For
    example, the three space position of a planet in orbit can be
    interpolated.

    @arg
    xkvec - 1 x n numpy.ndarray
    Independent variable data points
    fkvec - m x n numpy.ndarray
    Dependent variable data points
    fslope - m x 2 numpy.ndarray(optional)
    Function slope at boundary points
    customge - bool(optional)
    Specify to use the custom gauss elimination function.True
    to use the function, False use numpy's built in function.
    False by default.

    @return
    splineDataMat - m x n x 5 numpy.ndarray
    Spline coefficient data matrix.Organized by input data
    dimension, known value points, and coefficient.

    @author: Matt Marti
    @date: 2019-07-15
    */
    class Cubic_Spline {
    public:
        Cubic_Spline(Eigen::MatrixXd data);

        double operator()(double xinterp);
        Eigen::MatrixXd operator()(std::vector<double> xinterp);
        Eigen::MatrixXd operator()(Eigen::VectorXd xinterp);
        Eigen::MatrixXd operator()(Eigen::MatrixXd xinterp);

    private:
        std::vector<double> xvec;
        Eigen::MatrixXd avec;
        Eigen::MatrixXd bvec;
        Eigen::MatrixXd cvec;
        Eigen::MatrixXd dvec;
    };
}
