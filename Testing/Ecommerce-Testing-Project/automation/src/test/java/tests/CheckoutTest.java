package tests;

import base.BaseTest;
import org.testng.annotations.Test;
import pages.*;

public class CheckoutTest extends BaseTest {

    @Test
    public void checkoutTest() {
        LoginPage lp = new LoginPage(driver);
        lp.login("standard_user", "secret_sauce");

        ProductsPage pp = new ProductsPage(driver);
        pp.addProduct();
        pp.openCart();

        CheckoutPage cp = new CheckoutPage(driver);
        cp.checkout("John", "Doe", "600001");
    }
}