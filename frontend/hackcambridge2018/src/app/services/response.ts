export class PResponse {

    time:number;
    interest:number;
    duration:number;
    ts: Array<number>;
    is: Array<number>;
    ds: Array<number>;

    constructor(time:number, interest:number, duration:number, ts: Array<number>, is: Array<number>, ds: Array<number>){
        this.time = time;
        this.interest = interest;
        this.duration = duration;
        this.ts = ts;
        this.is = is;
        this.ds = ds;
    }
}