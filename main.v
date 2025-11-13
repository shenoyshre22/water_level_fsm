module water_level_controller (
    input wire clk, reset,
    input wire low, mid, high,
    output reg motor_on
);

    parameter EMPTY   = 2'b00;
    parameter FILLING = 2'b01;
    parameter FULL    = 2'b10;

    reg [1:0] current_state, next_state;

    // State transition
    always @(posedge clk or posedge reset) begin
        if (reset)
            current_state <= EMPTY;
        else
            current_state <= next_state;
    end

    // Next state logic
    always @(*) begin
        case (current_state)
            EMPTY: begin
                motor_on = 1;
                if (low && mid && high)
                    next_state = FULL;
                else
                    next_state = FILLING;
            end
            FILLING: begin
                motor_on = 1;
                if (high)
                    next_state = FULL;
                else
                    next_state = FILLING;
            end
            FULL: begin
                motor_on = 0;
                if (!high)
                    next_state = FILLING;
                else
                    next_state = FULL;
            end
            default: begin
                motor_on = 0;
                next_state = EMPTY;
            end
        endcase
    end
endmodule
