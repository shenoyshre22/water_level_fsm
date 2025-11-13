module tb_water_level_controller();
reg clk, reset;
reg low, mid, high;
wire motor_on;
water_level_controller uut (
.clk(clk), .reset(reset),
.low(low), .mid(mid), .high(high),
.motor_on(motor_on)
);
always #5 clk = ~clk;
initial begin
$dumpfile("water_level.vcd");
$dumpvars(0, tb_water_level_controller);
end
initial begin
clk=0; reset=1; low=0; mid=0; high=0;
#10 reset=0;
#20 low=1; mid=0; high=0;
#20 low=1; mid=1; high=0;
#20 low=1; mid=1; high=1;
#20 low=1; mid=0; high=0;
#20 low=0; mid=0; high=0;
#20 $finish;
end
initial begin
$monitor("Time=%0t | LOW=%b MID=%b HIGH=%b | MOTOR=%b",
$time, low, mid, high, motor_on);
end
endmodule